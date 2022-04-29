import logo from './logo.svg';
import './App.css';
import Main_tela from './main_tela';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom' 
import Criar_pessoa from './criar';


function App() {
  return (
    <Router>
        <Routes>
          <Route exact path="/" element={<Main_tela/>}/>
          <Route exact path="/criar" element={<Criar_pessoa/>}/>
        </Routes>
    </Router>
  );
}

export default App;
