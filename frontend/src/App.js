import React, { useState } from 'react';
import './App.css';

function App() {
  // Estados para los inputs
  const [correo, setCorreo] = useState('');
  const [nombre, setNombre] = useState('');
  const [enviar, setEnviar] = useState(false); // Estado para mostrar mensaje de éxito

  // Función que se ejecuta al hacer clic en "Enviar correo"
  const manejarClick = async () => {
    try {
      const respuesta = await fetch('http://localhost:8000/api/enviar-correo/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          correo: correo,
          nombre: nombre,
          vencimiento: '2025-07-31', // Puedes hacerlo dinámico si quieres
        }),
      });

      if (respuesta.ok) {
        setEnviar(true); // Mostrar mensaje de confirmación
      } else {
        alert('Error al enviar el correo.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error al conectar con el servidor.');
    }
  };

  return (
    <div className="contenedor">
      <h2>Enviar correo automático</h2>

      {/* Campo para nombre */}
      <input
        type="text"
        placeholder="Nombre del usuario"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
      />

      {/* Campo para correo */}
      <input
        type="email"
        placeholder="Correo electrónico"
        value={correo}
        onChange={(e) => setCorreo(e.target.value)}
      />

      {/* Botón para enviar */}
      <button onClick={manejarClick}>Enviar correo</button>

      {/* Mensaje después de enviar */}
      {enviar && (
        <p>
          ✅ Correo enviado a <strong>{correo}</strong> con el nombre <strong>{nombre}</strong>.
        </p>
      )}
    </div>
  );
}

export default App;
