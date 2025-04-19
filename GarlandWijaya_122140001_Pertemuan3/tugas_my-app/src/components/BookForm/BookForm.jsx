// src/components/BookForm/BookForm.js
import { useState, useContext } from "react";
import PropTypes from "prop-types";
import { BookContext } from "../../context/BookContext";
import "./BookForm.css";

const BookForm = ({ initialBook }) => {
  const { addBook, updateBook } = useContext(BookContext);
  const [title, setTitle] = useState(initialBook?.title || "");
  const [author, setAuthor] = useState(initialBook?.author || "");
  const [status, setStatus] = useState(initialBook?.status || "milik");
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!title.trim()) newErrors.title = "Judul harus diisi";
    if (!author.trim()) newErrors.author = "Penulis harus diisi";
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      const bookData = { title, author, status };
      if (initialBook) {
        updateBook({ ...initialBook, ...bookData });
      } else {
        addBook(bookData);
      }
      setTitle("");
      setAuthor("");
      setStatus("milik");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Judul"
      />
      {errors.title && <p className="error">{errors.title}</p>}

      <input
        value={author}
        onChange={(e) => setAuthor(e.target.value)}
        placeholder="Penulis"
      />
      {errors.author && <p className="error">{errors.author}</p>}

      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="milik">Dimiliki</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>

      <button type="submit">{initialBook ? "Update" : "Tambah"}</button>
    </form>
  );
};

BookForm.propTypes = {
  initialBook: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.string,
  }),
};

export default BookForm;
