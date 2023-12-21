package qtodo

import "fmt"

type Database interface {
	GetTaskList() []Task
	GetTask(string) (Task, error)
	SaveTask(Task) error
	DelTask(string) error
}

type DatabaseItem struct {
	tasks []Task
}

func (db *DatabaseItem) GetTaskList() []Task {
	return db.tasks
}

func (db *DatabaseItem) GetTask(taskName string) (Task, error) {
	for _, t := range db.tasks {
		if t.GetName() == taskName {
			return t, nil
		}
	}
	return nil, fmt.Errorf("%s not found", taskName)
}

func (db *DatabaseItem) SaveTask(task Task) error {
	for _, t := range db.tasks {
		if t.GetName() == task.GetName() {
			return fmt.Errorf("a task with the same name already exists")
		}
	}

	db.tasks = append(db.tasks, task)
	return nil
}

func (db *DatabaseItem) DelTask(taskName string) error {
	for idx, t := range db.tasks {
		if t.GetName() == taskName {
			db.tasks = append(db.tasks[:idx], db.tasks[idx+1:]...)
			return nil
		}
	}
	return fmt.Errorf("%s not found", taskName)
}

func NewDatabase() *DatabaseItem {
	db := &DatabaseItem{
		tasks: make([]Task, 0),
	}

	return db
}
