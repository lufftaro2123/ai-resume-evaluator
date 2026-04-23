import React, { useState } from "react";
import axios from "axios";

function UploadForm({ setData }) {
  const [files, setFiles] = useState([]);
  const [jd, setJd] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!files.length || !jd) {
      alert("Upload resumes and enter JD");
      return;
    }

    const formData = new FormData();
    files.forEach(file => formData.append("resumes", file));
    formData.append("jd", jd);

    try {
      setLoading(true);
      const res = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );
      setData(res.data);
    } catch (err) {
      console.error(err);
      alert("Error analyzing resumes");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Upload Resumes</h2>

      <input
        type="file"
        multiple
        className="input"
        onChange={(e) => setFiles([...e.target.files])}
      />

      <h2>Job Description</h2>

      <textarea
        rows="5"
        className="input"
        placeholder="Paste job description here..."
        value={jd}
        onChange={(e) => setJd(e.target.value)}
      />

      <br /><br />

      <button className="button" onClick={handleSubmit}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}

export default UploadForm;