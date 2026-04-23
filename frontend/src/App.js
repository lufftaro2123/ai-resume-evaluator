import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import Results from "./components/Results";
import "./App.css";

function App() {
  const [data, setData] = useState(null);

  return (
    <div className="app">
      <h1 className="title">AI Resume Evaluator</h1>

      <div className="card">
        <UploadForm setData={setData} />
      </div>

      {data && <Results data={data} />}
    </div>
  );
}

export default App;