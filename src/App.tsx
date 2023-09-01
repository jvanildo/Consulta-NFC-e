import { useState } from "react";
import axios from "axios";

function App() {
  const [selectedEmpresa, setSelectedEmpresa] = useState("");
  const [resultadoConsulta, setResultadoConsulta] = useState("");
  const [selectedDate, setSelectedDate] = useState("");
  const [loading, setLoading] = useState(false);

  const executarConsultaNfc = async () => {
    try {
      setLoading(true);
      setResultadoConsulta("");

      const response = await axios.post("http://127.0.0.1:5000/consultar-nfc", {
        parametro: selectedEmpresa,
        data: selectedDate,
      });
      setResultadoConsulta(response.data.message);
    } catch (error) {
      console.error("Erro ao executar consulta NFC:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container_input">
        <h1>Baixar NFC-e:</h1>
        
        <label>Data de consulta:</label>
        <input
          type="date"
          value={selectedDate}
          onChange={(e) => setSelectedDate(e.target.value)}
        />

        <select
          value={selectedEmpresa}
          onChange={(e) => setSelectedEmpresa(e.target.value)}
        >
          <option value="" disabled>
            Selecione a Empresa
          </option>
          <hr />
          <option value="FRANQUIA PRACA DE CASA FORTE">
            FRANQUIA PRACA DE CASA FORTE
          </option>
          <hr />
          <option value="FRANQUIA SHOPPING CARPINA">FRANQUIA SHOPPING CARPINA</option>
          <hr />
          <option value="FRANQUIA SHOPPING PLAZA">FRANQUIA SHOPPING PLAZA</option>
          <hr />
          <option value="FRANQUIA RIO MAR">FRANQUIA RIO MAR</option>
          <hr />
          <option value="FRISABOR FERREIRA COSTA IMBIRIBEIRA">FRISABOR FERREIRA COSTA IMBIRIBEIRA</option>
          <hr />
          <option value="FRISABOR FERREIRA COSTA JOAO PESSOA">FRISABOR FERREIRA COSTA JOAO PESSOA</option>
          <hr />
          <option value="FRISABOR MARCO ZERO">FRISABOR MARCO ZERO</option>
          <hr />
          <option value="FRISABOR BRENNAND PLAZA">FRISABOR BRENNAND PLAZA</option>
          <hr />
          <option value="FRISABOR BOA VISTA">FRISABOR BOA VISTA</option>
          <hr />
          <option value="all">TODAS AS EMPRESAS</option>
        </select>
        <button onClick={executarConsultaNfc} disabled={loading}>
          {loading ? "Carregando..." : "Executar Consulta NFC"}
        </button>
        <div>{resultadoConsulta}</div>
      </div>
    </div>
  );
}

export default App;
