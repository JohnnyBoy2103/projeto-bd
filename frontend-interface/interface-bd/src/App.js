import React, { useState } from 'react'
import './App.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import gotas from './assets/gotas.png'
import { api, requestAxios } from './api'

function App() {

  var now = new Date();
  var days = ['Dom','Seg','Ter','Qua','Qui','Sex','Sab'];
  var months = ['Jan','Feb','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'];
  const [drop, setDrop] = useState('')
  const [jaCliquei, setJaCliquei] = useState(false)
  const [dropText, setDropText] = useState('Selecione a query que deseja realizar...')
  const [disableInput, setDisableInput] = useState(true)
  const [placeholderInput, setPlaceholderInput] = useState('...')
  const [idQueryItem, setIdQueryItem] = useState('')
  const [idQuery, setIdQuery] = useState(1)
  const [query1, setQuery1] = useState([])
  const [query2, setQuery2] = useState([])
  const [query3, setQuery3] = useState([])
  const [query4, setQuery4] = useState([])
  const [query5, setQuery5] = useState([])
  const [query6, setQuery6] = useState([])

  const handleClickDropDown = () => {
    if (!jaCliquei) {
      setDrop('is-active')
      setJaCliquei(true)
    }
    else {
      setDrop('')
      setJaCliquei(false)
    }
  }

  const handleBlurDropDown = () => {
    setDrop('')
    setJaCliquei(false)
  }

  const handleValue = (e) => {
    setDropText(e.currentTarget.textContent)
    setDisableInput(false)
    setIdQuery(parseInt(e.currentTarget.id))
    if (e.currentTarget.id === '1')
      setPlaceholderInput('Digite o nome da Tag')
    else if (e.currentTarget.id === '2' || e.currentTarget.id === '5')
      setPlaceholderInput('Digite o nome da Empresa')
    else if (e.currentTarget.id === '3')
      setPlaceholderInput('Digite o nome do Aluno')
    else {
      setPlaceholderInput('...')
      setDisableInput(true)
    }
  }

  const handleChange = (e) => {
    setIdQueryItem(e.currentTarget.value)
  }

  const handleSubmit = () => {
    if (idQuery === 1) {
      requestAxios({
        url: api + `query-tags/${idQueryItem}`,
        method: 'get'
      })
      .then(response => {
        setQuery1(response.body)
      })
      .catch(err => {
        console.log(err)
      })
    }
    else if (idQuery === 2) {
      requestAxios({
        url: api + `query-vagas/${idQueryItem}`,
        method: 'get'
      })
      .then(response => {
        setQuery2(response.body)
      })
      .catch(err => {
        console.log(err)
      })
    }
    else if (idQuery === 3) {
      requestAxios({
        url: api + `query-historico/${idQueryItem}`,
        method: 'get'
      })
      .then(response => {
        if(JSON.stringify(response.body) === JSON.stringify({})) {
          setQuery3([])
        }
        else {
          setQuery3([response.body])
        }
      })
      .catch(err => {
        console.log(err)
      })
    }
    else if (idQuery === 4) {
      requestAxios({
        url: api + `vaga`,
        method: 'get'
      })
      .then(response => {
        setQuery4(response.body)
      })
      .catch(err => {
        console.log(err)
      })
    }
    else if (idQuery === 5) {
      requestAxios({
        url: api + `query-salario-medio/${idQueryItem}`,
        method: 'get'
      })
      .then(response => {
        setQuery5([response.body])
      })
      .catch(err => {
        console.log(err)
      })
    }
    else if (idQuery === 6) {
      requestAxios({
        url: api + `query-maiores-contratadoras`,
        method: 'get'
      })
      .then(response => {
        setQuery6(response.body)
      })
      .catch(err => {
        console.log(err)
      })
    }
  }

  return (
    <>
      <div className="app">
        <div className="Header">
          <span className="title-1">
            QUERIES
          </span>
          <span className="title-2">
            BANCO DE DADOS
          </span>
          <img src={gotas} className="img-gotas" alt="gotas"/>
          <span className="week-day">
            {days[now.getDay()]}
          </span>
          <span className="month-day">
            {months[now.getMonth()]} {now.getDate()}
          </span>
        </div>
        <span className="text1">
          SELECIONE A QUERY QUE DESEJA EXECUTAR
        </span>
        <div className="buttons">
          <button className="button is-success" onClick={handleSubmit}>Fazer Query!</button>
        </div>
        <div className="position-dropdown">
          <div className={`${"dropdown " + drop}`} onClick={handleClickDropDown} onBlur={handleBlurDropDown}>
            <div className="dropdown-trigger">
              <button className="button" aria-haspopup="true" aria-controls="dropdown-menu3">
                <span>{dropText}</span>
                <span className="icon is-small">
                  <FontAwesomeIcon icon="chevron-down" size="sm"></FontAwesomeIcon>
                </span>
              </button>
            </div>
            <div className="dropdown-menu" id="dropdown-menu3" role="menu">
              <div className="dropdown-content">
                <a id='1' href="#" className="dropdown-item" onMouseDown={handleValue}>
                  Visualizar empresas com uma determinada Tag
                </a>
                <a id='2' href="#" className="dropdown-item" onMouseDown={handleValue}>
                  Visualizar as vagas disponíveis numa empresa
                </a>
                <a id='3' href="#" className="dropdown-item" onMouseDown={handleValue}>
                  Visualizar a última empresa em que um aluno trabalhou
                </a>
                <a id='4' href="#" className="dropdown-item" onMouseDown={handleValue}>
                  Visualizar todas as vagas disponíveis
                </a>
                <a id='5' href="#" className="dropdown-item" onMouseDown={handleValue}>
                  Visualizar salário médio de uma empresa
                </a>
                <a id='6' href="#" className="dropdown-item" onMouseDown={handleValue}>
                  Visualizar as empresas com mais alunos contratados
                </a>
              </div>
            </div>
          </div>
        </div>
        <div className="text-box">
          <div className="control">
            <input className="input" type="text" disabled={disableInput} placeholder={placeholderInput} onChange={handleChange}/>
          </div>
        </div>
        <div className="table-position">
          <table className="table">
            <thead>
              {idQuery === 1 &&
                <tr>
                  <th>Nome</th>
                  <th>Email</th>
                  <th>Endereço</th>
                  <th>Telefone</th>
                  <th>Tags</th>
                  <th>Descrição</th>
                </tr>
              }
              {idQuery === 2 &&
                <tr>
                  <th>Título</th>
                  <th>Endereço</th>
                  <th>Auxílio</th>
                  <th>Descrição</th>
                </tr>
              }
              {idQuery === 3 &&
                <tr>
                  <th>Nome do Aluno</th>
                  <th>Email</th>
                  <th>Data de Início</th>
                  <th>Data de Término</th>
                  <th>Título da Vaga</th>
                  <th>Nome da Empresa</th>
                </tr>
              }
              {idQuery === 4 &&
                <tr>
                  <th>Título</th>
                  <th>Endereço</th>
                  <th>Auxílio</th>
                  <th>Descrição</th>
                </tr>
              }
              {idQuery === 5 &&
                <tr>
                  <th>Nome da empresa</th>
                  <th>Salário Médio</th>
                </tr>
              }
              {idQuery === 6 &&
                <tr>
                  <th>Nome da empresa</th>
                  <th>Quantidade de alunos</th>
                </tr>
              }
            </thead>
            <tbody>
              {idQuery === 1 &&
                query1.map((item) => 
                  <tr>
                    <td>{item["name"]}</td>
                    <td>{item["contact_email"]}</td>
                    <td>{item["address"]}</td>
                    <td>{item["phone_number"]}</td>
                    <td>{item["tags"].map(item_tag => {
                      return item_tag["name"] + ", "
                    })}</td>
                    <td>{item["description"]}</td>
                  </tr>
                )
              }
              {idQuery === 2 &&
                query2.map((item) => 
                  <tr>
                    <td>{item["title"]}</td>
                    <td>{item["location"]}</td>
                    <td>{item["grant"]}</td>
                    <td>{item["description"]}</td>
                  </tr>
                )
              }
              {idQuery === 3 &&
                query3.map((item) => 
                  <tr>
                    <td>{item["student"]["name"]}</td>
                    <td>{item["student"]["email"]}</td>
                    <td>{item["start_date"]}</td>
                    <td>{item["end_date"]}</td>
                    <td>{item["opportunity"]["title"]}</td>
                    <td>{item["opportunity"]["company"]['name']}</td>
                  </tr>
                )
              }
              {idQuery === 4 && query4 &&
                query4.map((item) => 
                  <tr>
                    <td>{item["title"]}</td>
                    <td>{item["location"]}</td>
                    <td>{item["grant"]}</td>
                    <td>{item["description"]}</td>
                  </tr>
                )
              }
              {idQuery === 5 && query5 &&
                query5.map((item) => 
                  <tr>
                    <td>{item["name"]}</td>
                    <td>{item["avg"]}</td>
                  </tr>
                )
              }
              {idQuery === 6 && query6 &&
                query6.map((item) => 
                  <tr>
                    <td>{item["name"]}</td>
                    <td>{item["count"]}</td>
                  </tr>
                )
              }
            </tbody>
          </table>
        </div>
      </div>
    </>
  )
}

export default App;
