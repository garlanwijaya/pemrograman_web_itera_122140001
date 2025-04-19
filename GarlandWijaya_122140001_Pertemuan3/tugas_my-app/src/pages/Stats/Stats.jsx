// src/pages/Stats/Stats.js
import useBookStats from "../../hooks/useBookStats";
import "./Stats.css";

const Stats = () => {
  const { totalBooks, owned, reading, toBuy } = useBookStats();

  return (
    <div>
      <h2>Statistik Buku</h2>
      <p>Total Buku: {totalBooks}</p>
      <p>Dimiliki: {owned}</p>
      <p>Sedang Dibaca: {reading}</p>
      <p>Ingin Dibeli: {toBuy}</p>
    </div>
  );
};

export default Stats;
