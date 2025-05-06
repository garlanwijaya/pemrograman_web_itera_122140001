/* eslint-disable no-undef */
// src/pages/Home/__tests__/Home.test.jsx
import { render, screen } from "@testing-library/react";
import Home from "../Home";

test("renders all components", () => {
  render(<Home />);

  expect(screen.getByPlaceholderText("Cari buku...")).toBeInTheDocument();
  expect(screen.getByRole("combobox")).toBeInTheDocument();
  expect(screen.getByText("Tambah")).toBeInTheDocument();
});
