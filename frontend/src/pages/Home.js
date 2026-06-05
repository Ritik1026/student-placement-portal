import React from 'react';

function Home() {
  return (
    <div className="container mx-auto p-8">
      <h1 className="text-4xl font-bold mb-4">Welcome to Placement Portal</h1>
      <p className="text-xl mb-8">AI-powered resume analysis and candidate shortlisting</p>
      <div className="grid grid-cols-2 gap-8">
        <div className="p-6 bg-blue-100 rounded">
          <h2 className="text-2xl font-bold mb-2">For Students</h2>
          <p>Upload your resume and get AI-powered feedback on quality and improvements</p>
        </div>
        <div className="p-6 bg-green-100 rounded">
          <h2 className="text-2xl font-bold mb-2">For Companies</h2>
          <p>Post jobs and get AI-shortlisted candidates matching your requirements</p>
        </div>
      </div>
    </div>
  );
}

export default Home;
