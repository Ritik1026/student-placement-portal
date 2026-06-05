import React, { useState } from 'react';

function StudentDashboard() {
  const [file, setFile] = useState(null);
  const [qualityScore, setQualityScore] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    // TODO: Upload resume to backend
    console.log('Uploading:', file);
  };

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">Student Dashboard</h1>
      
      <div className="bg-white p-6 rounded shadow">
        <h2 className="text-2xl font-bold mb-4">Upload Resume</h2>
        <div className="border-2 border-dashed border-gray-300 p-8 rounded text-center">
          <input 
            type="file" 
            onChange={handleFileChange} 
            accept=".pdf,.doc,.docx"
            className="block mx-auto"
          />
          {file && <p className="mt-4 text-green-600">File selected: {file.name}</p>}
          <button 
            onClick={handleUpload}
            className="mt-4 bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
          >
            Upload & Analyze
          </button>
        </div>
      </div>

      {qualityScore && (
        <div className="mt-8 bg-green-100 p-6 rounded">
          <h3 className="text-xl font-bold mb-2">Resume Quality Score</h3>
          <div className="text-4xl font-bold text-green-600">{qualityScore}%</div>
          <p className="mt-4">Your resume has been analyzed by AI. Check recommendations below.</p>
        </div>
      )}
    </div>
  );
}

export default StudentDashboard;
