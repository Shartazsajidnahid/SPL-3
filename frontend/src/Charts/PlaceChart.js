import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { Form, Container, Row, Col } from "react-bootstrap";
// import { useNavigate } from "react-router-dom";
import Chart from "chart.js/auto";
import "../App.css"

function PlaceChart({ type }) {
  const [chartType, setChartType] = useState(type);
  const [dataOption, setDataOption] = useState("occurrence");
  const [occurrencedata, setOccurrencedata] = useState([]);
  const [deathdata, setDeathdata] = useState([]);
  const [injurydata, setInjurydata] = useState([]);
  // const navigate = useNavigate();
  const chartRef = useRef(null);
  const chartDataRef = useRef(null);
  const myChartRef = useRef(null);
  const table_name = "district_info";
  const occurrence_type = "occurrence";
  const death_type = "dead";
  const injury_type = "injured";
  const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;


  const dataOptions = {
    occurrence: { data: occurrencedata, label: "Occurrences - District level", key: "typename" },
    injury: { data: injurydata, label: "Injuries - District level", key: "typename" },
    death: { data: deathdata, label: "Deaths - District level", key: "typename" },
  };

  useEffect(() => {
    // console.log("yes yes ");
    // console.log(vehicledata);
    // updateChart(chartType ,dataOption);
    updateChartAsync();
  }, [occurrencedata, injurydata, deathdata])
  
  const fetchOccurrenceData = async () => {
    await axios
      .get(`${apiBaseUrl}/graphchart/get-data-by-type?table_name=${table_name}&occurrence_type=${occurrence_type}`)
      .then((response) => {
        setOccurrencedata(response.data);
        // console.log(vehicledata);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const fetchDeathData = async () => {
    await axios
      .get(`${apiBaseUrl}/graphchart/get-data-by-type?table_name=${table_name}&occurrence_type=${death_type}`)
      .then((response) => {
        setDeathdata(response.data);
        // console.log(vehicledata);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const fetchInjuryData = async () => {
    await axios
      .get(`${apiBaseUrl}/graphchart/get-data-by-type?table_name=${table_name}&occurrence_type=${injury_type}`)
      .then((response) => {
        console.log("injury: ");
        console.log(response.data);
        setInjurydata(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(() => {
    fetchOccurrenceData();
    fetchDeathData();
    fetchInjuryData();
  }, []);

  const updateChartAsync = async () => {
    if (chartRef.current) {
      if (myChartRef.current) {
        myChartRef.current.destroy();
      }
      myChartRef.current = new Chart(chartRef.current, {
        type: chartType,
        data: chartDataRef.current,
        options: {
          maintainAspectRatio: false,
          responsive: true,
        },
      });
    }
    updateChart(chartType, dataOption)
  };

  useEffect(() => {
    
    updateChartAsync();
  }, [chartType, dataOption, occurrencedata]);
  
  const updateChart = (selectedChartType, selectedDataOption) => {
    
    const selectedData = dataOptions[selectedDataOption].data;
    const labelKey = dataOptions[selectedDataOption].key;
    console.log("update: ");
    const labels = selectedData.map((item) => item[labelKey]);
    const counts = selectedData.map((item) => item.count);
    console.log(labels);
    console.log(counts);
    let backgroundColors, border;

    if (selectedChartType === "pie") {
      // For Pie chart, let Chart.js use its default colors
      backgroundColors = undefined;
    } else {
      // For other chart types (e.g., bar, line), use your specified colors
      const colors = [
        
        "rgba(91, 8, 136,0.7)"
      ];

      backgroundColors = counts.map((count, index) => {
        const colorIndex = index % colors.length;
        return colors[colorIndex];
      });
    }

    if (selectedChartType === "line") {
        // For Pie chart, let Chart.js use its default colors
        border = 3;
    } else{
        border = undefined;
    }
  
    chartDataRef.current = {
      labels: labels,
      datasets: [
        {
          label: dataOptions[selectedDataOption].label,
          data: counts,
          borderWidth: border,
          backgroundColor: backgroundColors,
          borderJoinStyle: 'miter'
        },
      ],
    };
    myChartRef.current.config.type = selectedChartType;
    myChartRef.current.update();
  };


  return (
    <Container>
      <Row className="justify-content-center">
        <Col md={12} className=" p-2 rounded shadow custombackground">
          <Form>
            <Row>
              <Col md={4}>
              <h2 className="text-center">Districts</h2>
              </Col>
              <Col md={4}>
                <Form.Group controlId="chartType">
                  <Form.Control
                    as="select"
                    value={chartType}
                    onChange={(e) => {
                      const selectedChartType = e.target.value;
                      setChartType(selectedChartType);
                      updateChart(selectedChartType, dataOption);
                    }}
                  >
                    <option value="bar">Bar Chart</option>
                    <option value="pie">Pie Chart</option>
                    <option value="line">Line Chart</option>
                    <option value="radar">Radar Chart</option>
                  </Form.Control>
                </Form.Group>
              </Col>
              <Col md={4}>
                <Form.Group controlId="dataOption">
                  <Form.Control
                    as="select"
                    value={dataOption}
                    onChange={(e) => {
                      const selectedDataOption = e.target.value;
                      setDataOption(selectedDataOption);
                      updateChart(chartType, selectedDataOption);
                    }}
                  >
                    
                    <option value="occurrence">Occurrences</option>
                    <option value="injury">Injuries</option>
                    <option value="death">Deaths</option>
                  </Form.Control>
                </Form.Group>
              </Col>
            </Row>
          </Form>
        </Col>
      </Row>
      <Row className="justify-content-center mt-4">
        <Col md={12}>
        <canvas ref={chartRef} style={{ width: '100%', height: '100%' }}></canvas>
        {/* <canvas ref={chartRef} width="1000" height="230"></canvas> */}

        </Col>
      </Row>
    </Container>
  );
}

export default PlaceChart;
