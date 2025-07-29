import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from 'http://127.0.0.1:8000/api/axios';

export default function Login() {
const [form, setForm] = useState({ username: '', password: '' });
const [error, setError] = useState(null);
const navigate = useNavigate();

const handleChange = e => setForm({ ...form, [e.target.name]:
e.target.value });

const handleSubmit = async e => {
e.preventDefault();
try {
const res = await api.post('/login/', form);
localStorage.setItem('token', res.data.token);
navigate('/dashboard');
} catch {
setError('Usuario o contraseña incorrectos');
}
};

return (
<form onSubmit={handleSubmit}>
<h2>Iniciar Sesión</h2>
{error && <p style={{ color: 'red' }}>{error}</p>}
<input name='username' placeholder='Usuario'
value={form.username} onChange={handleChange} />
<input name='password' type='password' placeholder='Contraseña'
value={form.password} onChange={handleChange} />
<button type='submit'>Entrar</button>
</form>
);
}