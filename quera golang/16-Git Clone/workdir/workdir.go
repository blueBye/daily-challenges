package workdir

// you can use this library freely: "github.com/otiai10/copy"

type WorkDir struct {
}
package workdir

import (
	"errors"
	"log"
	"math/rand"
	"os"
	"path/filepath"
	"strings"

	cp "github.com/otiai10/copy"
)

const letterBytes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func RandStringBytes(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = letterBytes[rand.Intn(len(letterBytes))]
	}
	return string(b)
}

type WorkDir struct {
	path string
}

func InitEmptyWorkDir() *WorkDir {
	work_path := "project_" + RandStringBytes(10)
	if err := os.Mkdir(work_path, os.ModePerm); err != nil {
		log.Println(err)
	}
	return &WorkDir{path: work_path}
}

func (wd *WorkDir) CreateFile(name string) error {
	file_path := filepath.Join(wd.path, name)
	if _, err := os.Stat(file_path); errors.Is(err, os.ErrNotExist) {
		f, err := os.Create(file_path)
		if err != nil {
			return err
		}
		defer f.Close()
		return nil
	}
	return errors.New("file already exists")
}

func (wd *WorkDir) CreateDir(path string) error {
	dir_path := filepath.Join(wd.path, path)
	if _, err := os.Stat(dir_path); errors.Is(err, os.ErrNotExist) {
		if err := os.Mkdir(dir_path, os.ModePerm); err != nil {
			return err
		}
		return nil
	}
	return errors.New("directory already exists")
}

func (wd *WorkDir) WriteToFile(name string, content string) error {
	file_path := filepath.Join(wd.path, name)
	f, err := os.OpenFile(file_path, os.O_RDWR, 0660)
	if err != nil {
		return err
	}
	_, err = f.Write([]byte(content))
	return err
}

func (wd *WorkDir) ListFilesRoot() []string {
	files, _ := wd.ListFilesIn("")
	return files
}

func (wd *WorkDir) ListFilesIn(path string) ([]string, error) {
	files := []string{}
	base_path := filepath.Join(wd.path, path)
	err := filepath.Walk(base_path, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			parts := strings.Split(path, string(os.PathSeparator))
			files = append(files, strings.Join(parts[1:], "/"))
		}
		return nil
	})
	if err != nil {
		return nil, err
	}
	return files, nil
}

func (wd *WorkDir) CatFile(name string) (string, error) {
	file_path := filepath.Join(wd.path, name)
	_, err := os.OpenFile(file_path, os.O_RDWR, 0660)
	if err != nil {
		return "", err
	}
	content, err := os.ReadFile(file_path)
	return string(content), err
}

func (wd *WorkDir) AppendToFile(name string, content string) error {
	file_path := filepath.Join(wd.path, name)
	f, err := os.OpenFile(file_path, os.O_RDWR|os.O_APPEND, 0660)
	if err != nil {
		return err
	}
	_, err = f.Write([]byte(content))
	return err
}

func (wd *WorkDir) Clone() *WorkDir {
	clone := InitEmptyWorkDir()
	cp.Copy(wd.path, clone.path)
	return clone
}
