import React from "react";

function getColor(score) {
  if (score > 75) return "score-green";
  if (score > 50) return "score-yellow";
  return "score-red";
}

function CandidateCard({ candidate, rank }) {
  const strengths = candidate.insights?.strengths || [];
  const gaps = candidate.insights?.gaps || [];

  return (
    <div className="card">
      <h3>#{rank} — {candidate.filename}</h3>

      <p className={getColor(candidate.score)}>
        <strong>Score:</strong> {candidate.score}
      </p>

      <p>
        <strong>Summary:</strong> This candidate is a {candidate.score}% fit
      </p>

      <h4>Strengths</h4>
      <ul>
        {strengths.length ? (
          strengths.map((s, i) => <li key={i}>{s}</li>)
        ) : (
          <li>No strengths identified</li>
        )}
      </ul>

      <h4>Gaps</h4>
      <ul>
        {gaps.length ? (
          gaps.map((g, i) => <li key={i}>{g}</li>)
        ) : (
          <li>No gaps identified</li>
        )}
      </ul>
    </div>
  );
}

export default CandidateCard;