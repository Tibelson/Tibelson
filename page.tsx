'use client';
import { useState } from 'react';
import '../styles/home.css';

export default function LoginPage() {
  const [form, setForm] = useState({ email: '', password: '' });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Logging in with:', form);
  };

  return (
      <div className="home-container">
        <header className="nav-header">
          <h1>Login</h1>
        </header>

        <form onSubmit={handleSubmit} className="nav-links">
          <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
          <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
          <button type="submit">Login</button>
        </form>
      </div>
  );
}
