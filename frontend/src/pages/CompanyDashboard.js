import React, { useState } from 'react';

function CompanyDashboard() {
  const [jobs, setJobs] = useState([]);
  const [newJob, setNewJob] = useState({ title: '', description: '', skills: '' });

  const handlePostJob = () => {
    // TODO: Post job to backend
    console.log('Posting job:', newJob);
  };

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">Company Dashboard</h1>
      
      <div className="grid grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded shadow">
          <h2 className="text-2xl font-bold mb-4">Post New Job</h2>
          <input 
            type="text" 
            placeholder="Job Title" 
            className="w-full p-2 border rounded mb-4"
            value={newJob.title}
            onChange={(e) => setNewJob({...newJob, title: e.target.value})}
          />
          <textarea 
            placeholder="Job Description" 
            className="w-full p-2 border rounded mb-4 h-24"
            value={newJob.description}
            onChange={(e) => setNewJob({...newJob, description: e.target.value})}
          />
          <input 
            type="text" 
            placeholder="Required Skills (comma-separated)" 
            className="w-full p-2 border rounded mb-4"
            value={newJob.skills}
            onChange={(e) => setNewJob({...newJob, skills: e.target.value})}
          />
          <button 
            onClick={handlePostJob}
            className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700"
          >
            Post Job
          </button>
        </div>

        <div className="bg-white p-6 rounded shadow">
          <h2 className="text-2xl font-bold mb-4">Your Jobs</h2>
          {jobs.length === 0 ? (
            <p className="text-gray-500">No jobs posted yet</p>
          ) : (
            <ul>
              {jobs.map((job, idx) => (
                <li key={idx} className="mb-4 p-4 bg-gray-50 rounded">
                  <h3 className="font-bold">{job.title}</h3>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}

export default CompanyDashboard;
