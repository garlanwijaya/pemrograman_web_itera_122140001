// src/hooks/useBookStats.js
import { useContext } from "react";
import { BookContext } from "../context/BookContext";

const useBookStats = () => {
  const { books } = useContext(BookContext);

  const totalBooks = books.length;
  const owned = books.filter((book) => book.status === "milik").length;
  const reading = books.filter((book) => book.status === "baca").length;
  const toBuy = books.filter((book) => book.status === "beli").length;

  return { totalBooks, owned, reading, toBuy };
};

export default useBookStats;
