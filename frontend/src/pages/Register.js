import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Register() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    role: 'student'
  });
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    // TODO: Call register API
    console.log('Registering:', formData);
  };

  return (
    <div className="container mx-auto p-8 max-w-md">
      <div className="bg-white p-8 rounded shadow">
        <h1 className="text-3xl font-bold mb-6">Register</h1>
        <form onSubmit={handleRegister}>
          <input 
            type="text" 
            placeholder="Full Name" 
            className="w-full p-3 border rounded mb-4"
            value={formData.name}
            onChange={(e) => setFormData({...formData, name: e.target.value})}
            required
          />
          <input 
            type="email" 
            placeholder="Email" 
            className="w-full p-3 border rounded mb-4"
            value={formData.email}
            onChange={(e) => setFormData({...formData, email: e.target.value})}
            required
          />
          <input 
            type="password" 
            placeholder="Password" 
            className="w-full p-3 border rounded mb-4"
            value={formData.password}
            onChange={(e) => setFormData({...formData, password: e.target.value})}
            required
          />
          <select 
            className="w-full p-3 border rounded mb-6"
            value={formData.role}
            onChange={(e) => setFormData({...formData, role: e.target.value})}
          >
            <option value="student">Student</option>
            <option value="company">Company</option>
          </select>
          <button 
            type="submit"
            className="w-full bg-green-600 text-white py-3 rounded hover:bg-green-700"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
}

export default Register;
