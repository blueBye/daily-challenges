package commands

import (
	"errors"
	"regexp"
	"strconv"
	"vc/workdir"
)

type VC struct {
	wd     *workdir.WorkDir
	stage  *workdir.WorkDir
	head   *Commit
	branch []*Commit
	status StatusResult
}

type Commit struct {
	message string
	wd      *workdir.WorkDir
}

type StatusResult struct {
	StagedFiles   []string
	ModifiedFiles []string
}

func Init(wd *workdir.WorkDir) *VC {
	// wd is already cloned in test
	branch := []*Commit{{
		message: "__base__",
		wd:      workdir.InitEmptyWorkDir(),
	}}

	return &VC{
		wd:     wd,
		stage:  wd.Clone(),
		head:   branch[0],
		branch: branch,
		status: StatusResult{
			StagedFiles:   []string{},
			ModifiedFiles: wd.ListFilesRoot(),
		},
	}
}

func (vc *VC) Add(files ...string) {
	for _, file_name := range files {
		if _, err := vc.stage.CatFile(file_name); err != nil {
			vc.stage.CreateFile(file_name)
		}
		// add file name to staged filed if not alrady staged
		exists := false
		for _, f := range vc.status.StagedFiles {
			if f == file_name {
				exists = true
			}
		}
		if !exists {
			vc.status.StagedFiles = append(vc.status.StagedFiles, file_name)
		}

		content, _ := vc.wd.CatFile(file_name)
		vc.stage.WriteToFile(file_name, content)
	}
}

func (vc *VC) AddAll() {
	for _, file_name := range vc.status.ModifiedFiles {
		vc.Add(file_name)
	}
}

func (vc *VC) Commit(message string) {
	commit := Commit{
		message: message,
		wd:      vc.stage.Clone(),
	}
	vc.status.StagedFiles = nil
	vc.branch = append(vc.branch, &commit)
}

func (vc *VC) Status() StatusResult {
	// clear status.ModifiedFiles
	vc.status.ModifiedFiles = nil

	// update Modified files
	for _, file_name := range vc.wd.ListFilesRoot() {
		c, err := vc.stage.CatFile(file_name)
		modified := false
		if err != nil { // file does not exist in stage (created)
			modified = true
		} else {
			content, _ := vc.wd.CatFile(file_name)
			if c != content { // file was modified
				modified = true
			}
		}

		if modified {
			vc.status.ModifiedFiles = append(vc.status.ModifiedFiles, file_name)
		}
	}

	return vc.status
}

func (vc *VC) GetWorkDir() *workdir.WorkDir {
	return vc.wd
}

func (vc *VC) Log() []string {
	log := make([]string, 0)

	for i := len(vc.branch) - 1; i >= 1; i-- {
		log = append(log, vc.branch[i].message)
	}
	return log
}

func (vc *VC) Checkout(commit string) (*workdir.WorkDir, error) {
	switch commit[0] {
	case '~':
		re := regexp.MustCompile("^~([0-9]+)$")
		match := re.FindStringSubmatch(commit)
		rev_idx, _ := strconv.Atoi(match[1])
		return vc.branch[len(vc.branch)-1-rev_idx].wd, nil
	case '^':
		count := len(commit)
		return vc.branch[len(vc.branch)-1-count].wd, nil
	default:
		return nil, errors.New("not found")
	}
}
