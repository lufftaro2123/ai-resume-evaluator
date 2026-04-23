import React from "react";
import CandidateCard from "./CandidateCard";

function Results({ data }) {
  return (
    <div>
      <h2>Ranking</h2>

      {data.ranking.map((candidate, index) => (
        <CandidateCard
          key={index}
          candidate={candidate}
          rank={index + 1}
        />
      ))}
    </div>
  );
}

export default Results;