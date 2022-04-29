import React, { Component } from "react";
import axios from 'axios';
import { DataGrid } from '@mui/x-data-grid';
import Row_table from "./row_table";
import "./App.css"
import plus from './plus.png';
import Button from 'react-bootstrap/Button';
import { Modal } from "@mui/material";


export default class Main_tela extends Component {
    constructor(props) {
        super(props);

        this.state ={   
            tabela : []
            

        }
    }

    async componentDidMount(){
        const response_api = await axios.get("https://visie-pratico-teste.herokuapp.com/pessoas")
        this.setState({
            tabela:response_api.data
        })
       
        
    
}
    

    render()
     {
         
          const rows = [
            
          ];

          this.state.tabela.map(i=>
            rows.push({"id":i.id_pessoa,"nome":i.nome.split(' ')[0],"data_entrada":i.data_admissao.split("-")[2]+"/"+i.data_admissao.split("-")[1]+"/"+i.data_admissao.split("-")[0]}))

          
        
        return (
            <>
            <a href="/criar" > <img className="btn-criar" src={plus}></img></a>
            <div className="container">
              
	
	<div className="table">
		<div className="table-header">
			<div className="header__item"><a id="name" className="filter__link" href="#">NOME</a></div>
			<div className="header__item"><a id="data_admissao" className="filter__link filter__link--number" href="#">data de admissão</a></div>
			<div className="header__item"><a id="Excluir" className="filter__link filter__link--number" href="#">Excluir</a></div>
			<div className="header__item"><a id="Alterar" className="filter__link filter__link--number" href="#">Alterar</a></div>
		</div>
		<div className="table-content">	
        {rows.map(i=>{
     return <Row_table id = {i.id} nome = {i.nome} data_admissao = {i.data_entrada}/>
 })}
			
			</div>
		</div>	
	</div>
    
    </>

        )
        
    }
    
}
// {rows.map(i=>{
//     return <Row_table id = {i.id} nome = {i.nome} data_admissao = {i.data_entrada}/>
// })}