import React, { useState } from 'react';
import './App.css';

function App() {
  const [empresa, setEmpresa] = useState(''); //constantes para la caja donde va el texto
  const [enviar, setEnviar] = useState(false); //constante para el boton de enviar

  const manejarClick = () => {
    setEnviar(true); //cuando se hace click en el boton de enviar, se cambia el estado de enviar a true
  }

  //lo que se muestra en la pantalla
  return (
    <div style={{ padding: '20px'}}>
      <input 
      type="text"
      placeholder="Escribe el nombre de la empresa"
      value={empresa} //lo que aparece aqui es el nombre de la empresa pero debe aparecer que ya se envió el correo
      onChange={(e) => setEmpresa(e.target.value)} //actualiza la empresa al escribir
      />

    //al hacer click de activa manejarClick
    <button onClick={manejarClick} style={{marginLeft: '10px'}}>
      Enviar correo
    </button>


    //si enviar es true se muestra el nombre
    {enviar && (
      <p style={{marginTop:'20px'}}>
      Hola, se envió el correo a <strong>{empresa}</strong>
      </p>
    )}
    </div>
  );
}

export default App;
