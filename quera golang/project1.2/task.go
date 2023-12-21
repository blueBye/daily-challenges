package qtodo

import (
	"fmt"
	"time"
)

type Task interface {
	DoAction()
	GetAlarmTime() time.Time
	GetAction() func()
	GetName() string
	GetDescription() string
}

type TaskItem struct {
	name        string
	description string
	due         time.Time
	action      func()
}

func (taskItem *TaskItem) DoAction() {
	taskItem.action()
}

func (taskItem *TaskItem) GetAlarmTime() time.Time {
	return taskItem.due
}

func (taskItem *TaskItem) GetAction() func() {
	return taskItem.action
}

func (taskItem *TaskItem) GetName() string {
	return taskItem.name
}

func (taskItem *TaskItem) GetDescription() string {
	return taskItem.description
}

func NewTask(action func(), due time.Time, name string, description string) (*TaskItem, error) {
	if len(name) == 0 {
		return nil, fmt.Errorf("invalid task name")
	}
	if len(description) == 0 {
		return nil, fmt.Errorf("invalid task description")
	}
	if due.Before(time.Now()) {
		return nil, fmt.Errorf("invalid due date")
	}

	task := &TaskItem{
		name:        name,
		description: description,
		action:      action,
		due:         due,
	}

	return task, nil
}
