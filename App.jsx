import React, { useState } from 'react';
import './index.css'; // Use your existing styles from home.css

function App() {
  const [isLogin, setIsLogin] = useState(true);
  const [form, setForm] = useState({
    full_name: '',
    email: '',
    phone: '',
    password: ''
  });

  const toggleForm = () => {
    setIsLogin(!isLogin);
    setForm({ full_name: '', email: '', phone: '', password: '' });
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isLogin) {
      console.log('Logging in:', form);
    } else {
      console.log('Signing up:', form);
    }
  };

  return (
      <div className="home-container">
        <header className="nav-header">
          <div className="nav-links">
          </div>
        </header>

        <form onSubmit={handleSubmit} className="home-container">
          {!isLogin && (
              <>
                <input
                    type="text"
                    name="full_name"
                    placeholder="Full Name"
                    value={form.full_name}
                    onChange={handleChange}
                    required
                />
                <input
                    type="text"
                    name="phone"
                    placeholder="Phone Number"
                    value={form.phone}
                    onChange={handleChange}
                    required
                />
              </>
          )}
          <input
              type="email"
              name="email"
              placeholder="Email"
              value={form.email}
              onChange={handleChange}
              required
          />
          <input
              type="password"
              name="password"
              placeholder="Password"
              value={form.password}
              onChange={handleChange}
              required
          />
          <button type="submit">{isLogin ? 'Login' : 'Sign Up'}</button>
        </form>

        <div style={{ textAlign: 'center', marginTop: '1rem' }}>
          <button onClick={toggleForm}>
            {isLogin ? 'Need an account? Sign Up' : 'Already have an account? Login'}
          </button>
        </div>
      </div>
  );
}

export default App;
