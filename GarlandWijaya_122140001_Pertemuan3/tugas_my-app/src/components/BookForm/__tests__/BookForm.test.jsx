/* eslint-disable no-undef */
// src/components/BookForm/__tests__/BookForm.test.jsx
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { BookProvider } from "../../../context/BookContext";
import BookForm from "../BookForm";

test("validates form submission", async () => {
  render(
    <BookProvider>
      <BookForm />
    </BookProvider>
  );

  const submitBtn = screen.getByText("Tambah");
  userEvent.click(submitBtn);

  await waitFor(() => {
    expect(screen.getByText("Judul harus diisi")).toBeInTheDocument();
    expect(screen.getByText("Penulis harus diisi")).toBeInTheDocument();
  });
});
