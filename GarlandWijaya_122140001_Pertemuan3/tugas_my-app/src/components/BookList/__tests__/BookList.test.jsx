/* eslint-disable no-undef */
// src/components/BookList/__tests__/BookList.test.jsx
import { render, screen } from "@testing-library/react";
import { BookProvider } from "../../../context/BookContext";
import BookList from "../BookList";

test("renders empty state when no books", () => {
  render(
    <BookProvider>
      <BookList />
    </BookProvider>
  );

  expect(screen.getByText("Tidak ada buku yang ditemukan")).toBeInTheDocument();
});
