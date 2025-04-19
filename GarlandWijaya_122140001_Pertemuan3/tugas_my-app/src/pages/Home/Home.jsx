// src/pages/Home/Home.jsx
import { useContext, useState } from "react";
import { BookContext } from "../../context/BookContext";
import { Link, Routes, Route } from "react-router-dom";
import BookForm from "../../components/BookForm/BookForm";
import BookFilter from "../../components/BookFilter/BookFilter";
import BookList from "../../components/BookList/BookList";
import "./Home.css";

const Home = () => {
  const { setSearchTerm } = useContext(BookContext);
  const [selectedBook] = useState(null);

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  return (
    <div className="home-container">
      <nav>
        <Link to="/" className="link">
          Manajemen Buku
        </Link>
        <Link to="/stats" className="link">
          Statistik
        </Link>
      </nav>
      <div className="section-card">
        <h1 className="page-title">Manajemen Buku</h1>

        <div className="search-container">
          <input
            type="text"
            placeholder="Cari buku..."
            onChange={handleSearch}
            className="search-input"
          />
        </div>

        <div className="filter-wrapper">
          <BookFilter />
        </div>

        <div className="form-section">
          <BookForm initialBook={selectedBook} />
        </div>
      </div>

      <div className="book-section">
        <BookList />
      </div>
    </div>
  );
};

export default Home;
