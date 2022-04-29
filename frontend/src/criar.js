import React, { Component } from "react";
import axios from 'axios';
import { DataGrid } from '@mui/x-data-grid';
import Row_table from "./row_table";
import "./criar.css"






export default class Criar_pessoa extends Component {
    constructor(props) {
        super(props);

        this.state ={   
        }
    }

    async componentDidMount(){

}

  handleSubmit(event) {
  const nome=event.target.nome.value
  const rg=event.target.rg.value
  const  cpf=event.target.cpf.value
  const  data_nascimento=event.target.data_nascimento.value
  const  data_admissao=event.target.data_admissao.value
  const response = axios.post("https://visie-pratico-teste.herokuapp.com/pessoas?nome="+nome+"&rg="+rg+"&cpf="+cpf+"&data_nascimento="+data_nascimento+"&data_admissao="+data_admissao).catch(function (error) {
    if (error.response) {

      alert('Falha no cadastro, por favor reveja a data!!');
      document.location.href="/";
    }  else {
      console.log('Error', error.message);
      
    }
    console.log(error.config);
  });
  
  console.log(console.log(response))
  document.location.href="/";
  
   event.preventDefault();
}

cancelar(){
  document.location.href="/";
}


    render()
     {
          
          
        
        return (
            <div className="background_create">
            <div className="background">
            <div className="container_create">
              <div className="screen">
                <div className="screen-header">
                  <div className="screen-header-left">
                    <div className="screen-header-button close"></div>
                    <div className="screen-header-button maximize"></div>
                    <div className="screen-header-button minimize"></div>
                  </div>
                  <div className="screen-header-right">
                    <div className="screen-header-ellipsis"></div>
                    <div className="screen-header-ellipsis"></div>
                    <div className="screen-header-ellipsis"></div>
                  </div>
                </div>
                <div className="screen-body">
                  <div className="screen-body-item left">
                    <div className="app-title">
                      <span>CADASTRAR</span>
                    </div>
                  </div>
                  
                  <div className="screen-body-item">
                  <form onSubmit={this.handleSubmit}>
                    <div className="app-form">
                      <div className="app-form-group">
                        <input name="nome" className="app-form-control" placeholder="Nome Completo" required />
                      </div>
                      <div className="app-form-group">
                        <input name="rg" className="app-form-control" placeholder="RG" required/>
                      </div>
                      <div className="app-form-group">
                        <input name="cpf" className="app-form-control" placeholder="CPF" required/>
                      </div>
                      <div className="app-form-group">
                        <input name="data_nascimento" className="app-form-control" placeholder="DATA DE NASCIMENTO (yyyy-mm-dd)" required/>
                      </div>
                      <div className="app-form-group">
                        <input name="data_admissao" className="app-form-control" placeholder="DATA DE ADMISSAO (yyyy-mm-dd)" required/>
                      </div>
                      <div className="app-form-group">
                        <input name="funcao" className="app-form-control" placeholder="FUNÇÃO" required/>
                      </div>
                      
                      <div className="app-form-group buttons">
                        
                        <input className="app-form-button" name="submit" type="submit" value="SUBMIT"></input>
                        <a className="app-form-button-a" name = "cancel" onClick={() =>this.cancelar()}>CANCEL</a>
                      </div>
                    </div>
                    </form>
                  </div>
                  
                </div>
              </div>
              
            </div>
          </div>
          </div>
        

        )
        
    }
    
}
