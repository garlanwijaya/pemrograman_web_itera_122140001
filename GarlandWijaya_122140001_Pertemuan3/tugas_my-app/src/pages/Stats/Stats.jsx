// src/pages/Stats/Stats.js
import useBookStats from "../../hooks/useBookStats";
import { Link, Routes, Route } from "react-router-dom";
import "./Stats.css";

const Stats = () => {
  const { totalBooks, owned, reading, toBuy } = useBookStats();

  return (
    <>
      <nav>
        <Link to="/" className="link">
          Managemen Buku
        </Link>
        <Link to="/stats" className="link">
          Statistik
        </Link>
      </nav>
      <div>
        <h1>Statistik</h1>
        <div className="stats-grid">
          <div className="stat-card card-1">
            <h2 className="stat-title">Total Buku</h2>
            <p className="stat-value">{totalBooks}</p>
          </div>
          <div className="stat-card card-2">
            <h2 className="stat-title">Dimiliki</h2>
            <p className="stat-value">{owned}</p>
          </div>
          <div className="stat-card card-3">
            <h2 className="stat-title">Sedang Dibaca</h2>
            <p className="stat-value">{reading}</p>
          </div>
          <div className="stat-card card-4">
            <h2 className="stat-title">Ingin Dibeli</h2>
            <p className="stat-value">{toBuy}</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default Stats;
