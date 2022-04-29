import React, { Component } from "react";
import axios from 'axios';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

export default class Row_table extends Component {
    constructor(props) {
        super(props);

        this.state = {
            open: false,
            nome: "",
            rg: "",
            cpf: "",
            data_nascimento: "",
            data_admissao: "",
            funcao: "",
            id_pessoa:""

        }
    }

    async componentDidMount() {

    }

    async remover(id) {
        const response = await axios.delete("/api/pessoas?id_api=" + id)
        console.log(response.data)
        window.location.reload(false);
    }


    async alterar(id) {
        console.log("alterar id : ")
        console.log(id)
        const response = await axios.get("/api/pessoas/" + id)
        const dados = response.data[0]


        this.setState({
            open: true,
            id_pessoa : dados.id_pessoa,
            nome: dados.nome,
            rg: dados.rg,
            cpf: dados.cpf,
            data_nascimento: dados.data_nascimento,
            data_admissao: dados.data_admissao,
            funcao: dados.funcao,


        })


    }
    handleClose() {
        this.setState({ open: false })
    }


    onNameChange(value) {
        this.setState({
            nome: value,
        });
    }

    onRgChange(value) {
        this.setState({
            rg: value,
        });
    }

    oncpfChange(value) {
        this.setState({
            cpf: value,
        });
    }

    ondata_nascimentoChange(value) {
        this.setState({
            data_nascimento: value,
        });
    } ondata_admissaoChange(value) {
        this.setState({
            data_admissao: value,
        });
    } onfuncaoChange(value) {
        this.setState({
            funcao: value,
        });
    }

    async alterar_dados() {
        
        console.log(this.state.nome)
        const res = await axios.put('/api/pessoas?id_pessoa=' +this.props.id + '&nome=' + this.state.nome+'&rg='+this.state.rg+"&cpf="+this.state.cpf+'&data_nascimento='+this.state.data_nascimento+"&data_admissao="+this.state.data_admissao+"&funcao="+this.state.funcao)
        window.location.reload(false);
    }



    render() {
        const style = {
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: 400,
            bgcolor: 'background.paper',
            border: '2px solid #000',
            boxShadow: 24,
            p: 4,
        };


        return (
            
            <div class="table-row">
                <div class="table-data">{this.props.nome}</div>
                <div class="table-data">{this.props.data_admissao}</div>
                <div class="table-data"><button onClick={() => this.remover(this.props.id)}><img src="https://cdn-icons-png.flaticon.com/16/216/216658.png"></img>Remover</button></div>
                <div class="table-data"><button onClick={() => this.alterar(this.props.id)}><img src="https://cdn-icons-png.flaticon.com/16/1159/1159633.png"></img>Alterar</button></div>


                <Modal
                    open={this.state.open}
                    onClose={this.handleClose}
                    aria-labelledby="modal-modal-title"
                    aria-describedby="modal-modal-description"
                >
                    <Box sx={style}>
                        <Typography id="modal-modal-title" variant="h6" component="h2">
                            Alterar
                        </Typography>
                        <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                            <div className="app-form-group">
                                <input name="nome" className="app-form-control-editar" placeholder="Nome Completo" value={this.state.nome} onChange={e => this.onNameChange(e.target.value)} />
                            </div>
                            <div className="app-form-group">
                                <input name="rg" className="app-form-control-editar" placeholder="RG" value={this.state.rg} onChange={e => this.onRgChange(e.target.value)} />
                            </div>
                            <div className="app-form-group">
                                <input name="cpf" className="app-form-control-editar" placeholder="CPF" value={this.state.cpf} onChange={e => this.oncpfChange(e.target.value)} />
                            </div>
                            <div className="app-form-group">
                                <input name="data_nascimento" className="app-form-control-editar" placeholder="DATA DE NASCIMENTO" value={this.state.data_nascimento} onChange={e => this.ondata_nascimentoChange(e.target.value)} />
                            </div>
                            <div className="app-form-group">
                                <input name="data_admissao" className="app-form-control-editar" placeholder="DATA DE ADMISSAO" value={this.state.data_admissao} onChange={e => this.ondata_admissaoChange(e.target.value)} />
                            </div>
                            <div className="app-form-group">
                                <input name="funcao" className="app-form-control-editar" placeholder="FUNÇÃO" value={this.state.funcao} onChange={e => this.onfuncaoChange(e.target.value)} />
                            </div>

                            <br />
                            <Button onClick={() =>this.alterar_dados()}>Salvar</Button>
                            <Button onClick={() => this.setState({ open: false })}>Fechar</Button>
                        </Typography>
                    </Box>
                </Modal>
            </div>


        )

    }

}
