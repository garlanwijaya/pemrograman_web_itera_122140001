/* eslint-disable no-undef */
// src/pages/Stats/__tests__/Stats.test.jsx
import { render, screen } from "@testing-library/react";
import { BookProvider } from "../../context/BookContext";
import Stats from "../Stats";

test("shows correct statistics", () => {
  render(
    <BookProvider>
      <Stats />
    </BookProvider>
  );

  expect(screen.getByText("Total Buku: 0")).toBeInTheDocument();
  expect(screen.getByText("Dimiliki: 0")).toBeInTheDocument();
});
