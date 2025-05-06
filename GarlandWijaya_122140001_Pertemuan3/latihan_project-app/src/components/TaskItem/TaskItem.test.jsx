/* eslint-disable no-undef */
import React from "react";
import { render, screen, fireEvent, cleanup } from "@testing-library/react";
import TaskItem from "./TaskItem";

describe("TaskItem Component", () => {
  const mockTask = {
    id: 1,
    title: "Test Task",
    completed: false,
  };

  const mockOnDelete = jest.fn();
  const mockOnToggleComplete = jest.fn();

  beforeEach(() => {
    render(
      <TaskItem
        task={mockTask}
        onDelete={mockOnDelete}
        onToggleComplete={mockOnToggleComplete}
      />
    );
  });

  afterEach(() => {
    cleanup();
  });

  it("renders task title", () => {
    expect(screen.getByText("Test Task")).toBeInTheDocument();
  });

  it("calls onToggleComplete when checkbox is clicked", async () => {
    await fireEvent.click(screen.getByRole("checkbox"));
    expect(mockOnToggleComplete).toHaveBeenCalledWith(1);
  });

  it("calls onDelete when delete button is clicked", async () => {
    await fireEvent.click(screen.getByText("Delete"));
    expect(mockOnDelete).toHaveBeenCalledWith(1);
  });

  it("shows completed style when task is completed", () => {
    const completedTask = { ...mockTask, completed: true };
    rerender(
      <TaskItem
        task={completedTask}
        onDelete={mockOnDelete}
        onToggleComplete={mockOnToggleComplete}
      />
    );

    const taskItem = screen.getByText("Test Task").closest(".task-item");
    expect(taskItem).toHaveClass("completed");
  });
});
