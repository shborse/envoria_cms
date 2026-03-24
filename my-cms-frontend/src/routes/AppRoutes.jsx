import React from "react";
import { Routes, Route } from "react-router-dom";
import HomePage from "../pages/HomePage";
import AboutPage from "../pages/AboutPage";
import ServicesPage from "../pages/ServicesPage";
import CoursesPage from "../pages/CoursesPage";
import CareersPage from "../pages/CareersPage";
import ContactPage from "../pages/ContactPage";
import AdmissionPage from "../pages/AdmissionPage";
import InternshipPage from "../pages/InternshipPage";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="/services" element={<ServicesPage />} />
      <Route path="/courses" element={<CoursesPage />} />
      <Route path="/careers" element={<CareersPage />} />
      <Route path="/contact" element={<ContactPage />} />
      <Route path="/admission" element={<AdmissionPage />} />
      <Route path="/internship" element={<InternshipPage />} />
    </Routes>
  );
};

export default AppRoutes;