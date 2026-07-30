from services.roadmap_service import gerar_roadmap


def mostrar_roadmap(usuario_id: int):
    dados = gerar_roadmap(usuario_id)

    print("\n══════════════ 🛣 ROADMAP ══════════════")

    print(f"\n🎯 Objetivo: {dados['objetivo'] or 'Não definido'}")

    barras = dados["progresso"] // 10
    barra = "█" * barras + "░" * (10 - barras)

    print(f"\n📈 Evolução: [{barra}] {dados['progresso']}%")

    print(f"\n⭐ XP: {dados['xp']}")
    print(f"🧠 Quizzes: {dados['quizzes']}")

    print("\n📚 Próximas etapas:\n")

    for i, etapa in enumerate(dados["etapas"], start=1):
        print(f"{i}. {etapa}")

    input("\nPressione ENTER para voltar...")