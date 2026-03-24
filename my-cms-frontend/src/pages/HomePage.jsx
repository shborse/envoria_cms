import React, { useEffect, useState } from "react";
import "./HomePage.css";

const HomePage = () => {
  const [homeData, setHomeData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/home/")
      .then((res) => res.json())
      .then((data) => setHomeData(data))
      .catch((err) => console.log(err));
  }, []);

  if (!homeData) return <h2>Loading...</h2>;

  return (
    <div>

      {/* Navbar */}
      <header className="navbar">
        <h2>Enorvia CMS</h2>
      </header>

      {/* Hero (FROM BACKEND) */}
      <section className="hero">
        <h1>{homeData.hero_title}</h1>
        <h3>{homeData.hero_subtitle}</h3>
        <p>{homeData.hero_description}</p>
      </section>

      {/* Static sections (safe for prototype) */}
      <section className="pillars">
        <h2>Our Pillars</h2>
        <div className="pillar-list">
          <div className="pillar-card">
            <h4>Innovation</h4>
            <p>We focus on cutting-edge solutions.</p>
          </div>
          <div className="pillar-card">
            <h4>Learning</h4>
            <p>Hands-on practical education.</p>
          </div>
          <div className="pillar-card">
            <h4>Growth</h4>
            <p>Career-focused development.</p>
          </div>
        </div>
      </section>

      <section className="stats">
        <div className="stats-list">
          <div className="stat-card">
            <h3>500+</h3>
            <p>Students</p>
          </div>
          <div className="stat-card">
            <h3>50+</h3>
            <p>Projects</p>
          </div>
          <div className="stat-card">
            <h3>20+</h3>
            <p>Partners</p>
          </div>
        </div>
      </section>

    </div>
  );
};

export default HomePage;