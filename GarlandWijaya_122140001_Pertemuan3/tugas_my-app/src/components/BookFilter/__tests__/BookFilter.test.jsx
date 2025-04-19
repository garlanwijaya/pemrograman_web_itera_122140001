/* eslint-disable no-undef */
// src/components/BookFilter/__tests__/BookFilter.test.jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { BookProvider } from "../../../context/BookContext";
import BookFilter from "../BookFilter";

test("renders filter component and handles status change", async () => {
  render(
    <BookProvider>
      <BookFilter />
    </BookProvider>
  );

  const select = screen.getByRole("combobox");
  expect(select).toBeInTheDocument();

  await userEvent.selectOptions(select, "baca");
  expect(select).toHaveValue("baca");
});
