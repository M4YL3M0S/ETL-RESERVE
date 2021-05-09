class Viagens (object):

    def __init__(self,ID, TipoServico, Status, Criador, excluido, DataCriacao, DataModificacao,
                 DataExclusao, IDEmpresa, NomeEmpresa, IDEmpresaOriginal, NomeEmpresaOriginal, IDEmpresaFaturada,
                 NomeEmpresaFaturada, IDSolicitante, NomeSolicitante, IDConsultor, NomeConsultor, FormaPagtoCliente,
                 FormaPagtoFornecedor, DataAutorizacao, AtorAutorizacao, IDAutorizador, NomeAutorizador,
                 StatusAutorizacao, CodAutorizacao, DataEmissao, LocalEmissao, Emissor, TipoEmissao,
                 Remarcacao, IDPedidoRemarcacao, ReservaEscolhida, IDCentroCustoAMarcacao, TotalFee, idGrupoFee,
                 IdAutorizadorNotificado, Origem, CodAutorizacaoCartao, UltDigitosCartao, TipoEmissaoOnline,
                 IDEmissor, PerfilFee, QuantidadePAX,QuantidadePAXAutorizados, IDPedidoMulta, IDPedidoCredito,
                 CriadoPeloProduto, IDAutorizadorDelegado, UtilizarBilhetesNaoVoados, REM_IDPlano,
                 Integrado, ReferenciaTitulo):
        self.ID = ID
        self.TipoServico = TipoServico
        self.Status = Status
        self.Criador = Criador
        self.excluido = excluido
        self.DataCriacao = DataCriacao
        self.DataModificacao = DataModificacao
        self.DataExclusao = DataExclusao
        self.IDEmpresa = IDEmpresa
        self.NomeEmpresa = NomeEmpresa
        self.IDEmpresaOriginal = IDEmpresaOriginal
        self.NomeEmpresaOriginal = NomeEmpresaOriginal
        self.IDEmpresaFaturada = IDEmpresaFaturada
        self.NomeEmpresaFaturada = NomeEmpresaFaturada
        self.IDSolicitante = IDSolicitante
        self.NomeSolicitante = NomeSolicitante
        self.IDConsultor = IDConsultor
        self.NomeConsultor = NomeConsultor
        self.FormaPagtoCliente = FormaPagtoCliente
        self.FormaPagtoFornecedor = FormaPagtoFornecedor
        self.DataAutorizacao = DataAutorizacao
        self.AtorAutorizacao = AtorAutorizacao
        self.IDAutorizador = IDAutorizador
        self.NomeAutorizador = NomeAutorizador
        self.StatusAutorizacao = StatusAutorizacao
        self.CodAutorizacao = CodAutorizacao
        self.DataEmissao = DataEmissao
        self.LocalEmissao = LocalEmissao
        self.Emissor = Emissor
        self.TipoEmissao = TipoEmissao
        self.Remarcacao = Remarcacao
        self.IDPedidoRemarcacao = IDPedidoRemarcacao
        self.ReservaEscolhida = ReservaEscolhida
        self.IDCentroCustoAMarcacao = IDCentroCustoAMarcacao
        self.TotalFee = TotalFee
        self.idGrupoFee = idGrupoFee
        self.IdAutorizadorNotificado = IdAutorizadorNotificado
        self.Origem = Origem
        self.CodAutorizacaoCartao = CodAutorizacaoCartao
        self.UltDigitosCartao = UltDigitosCartao
        self.TipoEmissaoOnline = TipoEmissaoOnline
        self.IDEmissor = IDEmissor
        self.PerfilFee = PerfilFee
        self.QuantidadePAX = QuantidadePAX
        self.QuantidadePAXAutorizados = QuantidadePAXAutorizados
        self.IDPedidoMulta = IDPedidoMulta
        self.IDPedidoCredito = IDPedidoCredito
        self.CriadoPeloProduto = CriadoPeloProduto
        self.IDAutorizadorDelegado = IDAutorizadorDelegado
        self.UtilizarBilhetesNaoVoados = UtilizarBilhetesNaoVoados
        self.REM_IDPlano = REM_IDPlano
        self.Integrado = Integrado
        self.ReferenciaTitulo = ReferenciaTitulo


    def as_list(self):
        return [self.ID, self.TipoServico, self.Status, self.Criador, self.excluido, self.DataCriacao,
                self.DataModificacao,self.DataExclusao, self.IDEmpresa, self.NomeEmpresa, self.IDEmpresaOriginal,
                self.NomeEmpresaOriginal, self.IDEmpresaFaturada, self.NomeEmpresaFaturada,
                self.IDSolicitante, self.NomeSolicitante, self.IDConsultor, self.NomeConsultor,
                self.FormaPagtoCliente, self.FormaPagtoFornecedor, self.DataAutorizacao,
                self.AtorAutorizacao, self.IDAutorizador, self.NomeAutorizador,
                self. StatusAutorizacao, self.CodAutorizacao, self.DataEmissao, self.LocalEmissao,
                self.Emissor, self.TipoEmissao, self.Remarcacao, self.IDPedidoRemarcacao, self.ReservaEscolhida,
                self.IDCentroCustoAMarcacao, self.TotalFee, self.idGrupoFee, self.IdAutorizadorNotificado,
                self.Origem, self.CodAutorizacaoCartao, self.UltDigitosCartao, self.TipoEmissaoOnline,
                self.IDEmissor, self.PerfilFee, self.QuantidadePAX, self.QuantidadePAXAutorizados, self.IDPedidoMulta, self.IDPedidoCredito,
                self.CriadoPeloProduto, self.IDAutorizadorDelegado, self.UtilizarBilhetesNaoVoados,
                self.REM_IDPlano, self.Integrado, self.ReferenciaTitulo]