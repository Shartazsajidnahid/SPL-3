import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"; // Import Router and related components
// index.js or another entry point
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";

import "./App.css";
import Allnews from "./News/Allnews";
import NewsArticleDetails from "./News/NewsArticleDetails";
import Demo from "./Demo";
import Navbar from "./Navbar";
import SelectChartType from "./SelectChartType";
import SearchedNews from "./News/SearchedNews";
import VehicleChart from "./Charts/VehicleChart";
import Dashboard from "./VisualizeDashboard"
import TimeChart from "./Charts/TimeChart";
import DivisionChart from "./Charts/DivisionChart";
import Heatchart from "./Heatchart/Heatchart"
import Heatmap from "./Heatmap";
// import Newsdetail from "./News/Newsdetail";

function App() {
  return (
    // <Demo></Demo>
    <>
      <Router>
        <Navbar></Navbar>
        <div>
          <Routes>
            <Route path="/allnews" element={<Allnews />} />
            <Route path="/" element={<Allnews />} />
            <Route path="/news-article/:id" element={<NewsArticleDetails />} />
            <Route path="/searchednews" element={<SearchedNews />} />
            <Route path="/vehicleChart" element={<VehicleChart type="bar"/>} />
            <Route path="/timeChart" element={<TimeChart type="bar" />} />
            <Route path="/divisionChart" element={<DivisionChart type="bar" />} />

            <Route path="/visualizeDashboard" element={<Dashboard/>} />
            <Route path="/selectChartType" element={<SelectChartType />} />
            <Route path="heat" element={<Heatchart />} />

            <Route path="/heatmap" element={<Heatmap height="750px" width="700px"/>} />
          </Routes>
        </div>
      </Router>
    </>
  );
}

export default App;
