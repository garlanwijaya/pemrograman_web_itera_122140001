// src/components/BookList/BookList.js
import { useContext } from "react";
import PropTypes from "prop-types";
import { BookContext } from "../../context/BookContext";
import "./BookList.css";

const BookList = () => {
  const { books, filterStatus, searchTerm, deleteBook } =
    useContext(BookContext);
  const filteredBooks = books.filter((book) => {
    const statusMatch = filterStatus === "all" || book.status === filterStatus;
    const searchMatch =
      book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      book.author.toLowerCase().includes(searchTerm.toLowerCase());
    return statusMatch && searchMatch;
  });

  return (
    <div className="book-list">
      {filteredBooks.map((book) => (
        <div className="book-card" key={book.id}>
          <div className="book-item">
            <h3>{book.title}</h3>
            <p>Penulis: {book.author}</p>
            <p>
              Status:
              <span className={`status-tag ${book.status}`}>
                {book.status === "milik" && "Dimiliki"}
                {book.status === "baca" && "Sedang Dibaca"}
                {book.status === "beli" && "Ingin Dibeli"}
              </span>
            </p>
            <button className="delete-btn" onClick={() => deleteBook(book.id)}>
              Hapus
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

BookList.propTypes = {
  books: PropTypes.arrayOf(PropTypes.object),
  filterStatus: PropTypes.string,
  searchTerm: PropTypes.string,
  deleteBook: PropTypes.func,
};

export default BookList;
