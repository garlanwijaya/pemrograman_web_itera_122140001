// src/components/BookFilter/BookFilter.js
import { useContext } from "react";
import PropTypes from "prop-types";
import { BookContext } from "../../context/BookContext";
import "./BookFilter.css";

const BookFilter = () => {
  const { filterStatus, setFilterStatus } = useContext(BookContext);

  return (
    <select
      value={filterStatus}
      onChange={(e) => setFilterStatus(e.target.value)}
    >
      <option value="all">Semua</option>
      <option value="milik">Dimiliki</option>
      <option value="baca">Sedang Dibaca</option>
      <option value="beli">Ingin Dibeli</option>
    </select>
  );
};

BookFilter.propTypes = {
  filterStatus: PropTypes.string,
  setFilterStatus: PropTypes.func,
};

export default BookFilter;
