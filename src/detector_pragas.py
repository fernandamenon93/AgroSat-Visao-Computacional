import argparse
import csv
from datetime import datetime
from pathlib import Path

import cv2
import numpy as np


class AgroSatDetector:
    """Detector simples de sinais visuais associados a pragas/doencas em folhas.

    A inferencia visual usa OpenCV para:
    1. segmentar regioes verdes da imagem, simulando area de lavoura/folha;
    2. procurar manchas amarelas e marrons dentro dessa area;
    3. calcular um nivel de risco com base na porcentagem afetada;
    4. desenhar caixas, status e recomendacoes em tempo real.
    """

    def __init__(self, min_area=120):
        self.min_area = min_area

    def inferir(self, frame):
        frame = cv2.resize(frame, (960, 540))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Segmentacao da vegetacao: tons de verde.
        verde_baixo = np.array([30, 35, 35])
        verde_alto = np.array([90, 255, 255])
        mascara_verde = cv2.inRange(hsv, verde_baixo, verde_alto)

        # Possiveis sinais de estresse: manchas amareladas e marrons.
        amarelo_baixo = np.array([18, 60, 60])
        amarelo_alto = np.array([35, 255, 255])
        mascara_amarela = cv2.inRange(hsv, amarelo_baixo, amarelo_alto)

        marrom_baixo = np.array([5, 45, 20])
        marrom_alto = np.array([20, 255, 180])
        mascara_marrom = cv2.inRange(hsv, marrom_baixo, marrom_alto)

        # A inferencia considera somente manchas proximas de regioes verdes.
        kernel = np.ones((5, 5), np.uint8)
        mascara_verde_dilatada = cv2.dilate(mascara_verde, kernel, iterations=2)
        mascara_manchas = cv2.bitwise_or(mascara_amarela, mascara_marrom)
        mascara_manchas = cv2.bitwise_and(mascara_manchas, mascara_verde_dilatada)
        mascara_manchas = cv2.morphologyEx(mascara_manchas, cv2.MORPH_OPEN, kernel)
        mascara_manchas = cv2.morphologyEx(mascara_manchas, cv2.MORPH_CLOSE, kernel)

        area_verde = int(cv2.countNonZero(mascara_verde))
        area_manchas = int(cv2.countNonZero(mascara_manchas))
        percentual_afetado = (area_manchas / area_verde * 100) if area_verde > 0 else 0

        if area_verde < 1500:
            status = "SEM LAVOURA/FOLHA DETECTADA"
            risco = "Indefinido"
            recomendacao = "Aproxime a folha ou melhore a iluminacao."
            cor = (160, 160, 160)
        elif percentual_afetado < 3:
            status = "LAVOURA SAUDAVEL"
            risco = "Baixo"
            recomendacao = "Continuar monitoramento preventivo."
            cor = (0, 180, 0)
        elif percentual_afetado < 10:
            status = "ALERTA: POSSIVEL PRAGA/ESTRESSE"
            risco = "Medio"
            recomendacao = "Verificar a area e acompanhar evolucao."
            cor = (0, 180, 255)
        else:
            status = "RISCO ALTO: ACAO RECOMENDADA"
            risco = "Alto"
            recomendacao = "Acionar manejo e inspecionar a lavoura."
            cor = (0, 0, 255)

        frame_saida = frame.copy()
        contornos, _ = cv2.findContours(mascara_manchas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area >= self.min_area:
                x, y, w, h = cv2.boundingRect(contorno)
                cv2.rectangle(frame_saida, (x, y), (x + w, y + h), cor, 2)
                cv2.putText(frame_saida, "anomalia", (x, max(y - 8, 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor, 2)

        self._desenhar_painel(frame_saida, status, risco, percentual_afetado, recomendacao, cor)
        return frame_saida, {
            "status": status,
            "risco": risco,
            "percentual_afetado": percentual_afetado,
            "area_verde": area_verde,
            "area_manchas": area_manchas,
            "recomendacao": recomendacao,
        }

    @staticmethod
    def _desenhar_painel(frame, status, risco, percentual, recomendacao, cor):
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (960, 118), (20, 20, 20), -1)
        cv2.addWeighted(overlay, 0.75, frame, 0.25, 0, frame)

        cv2.putText(frame, "AgroSat - Visao Computacional", (20, 32),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, f"Status: {status}", (20, 64),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.68, cor, 2)
        cv2.putText(frame, f"Risco: {risco} | Area afetada estimada: {percentual:.2f}%", (20, 92),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.62, (255, 255, 255), 2)
        cv2.putText(frame, f"Recomendacao: {recomendacao}", (20, 115),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (230, 230, 230), 1)


def criar_video_sintetico(caminho_saida: Path):
    """Cria um video simples para testar o projeto sem webcam."""
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(caminho_saida), fourcc, 20, (960, 540))

    for i in range(160):
        frame = np.zeros((540, 960, 3), dtype=np.uint8)
        frame[:] = (45, 95, 45)
        cv2.putText(frame, "Video teste - folha/lavoura simulada", (150, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # folha verde
        cv2.ellipse(frame, (480, 300), (260, 150), 0, 0, 360, (35, 155, 35), -1)
        cv2.line(frame, (230, 300), (730, 300), (25, 110, 25), 6)

        # manchas aumentando ao longo do video
        qtd = 3 + i // 18
        rng = np.random.default_rng(42)
        for n in range(qtd):
            x = int(300 + rng.integers(0, 360))
            y = int(210 + rng.integers(0, 170))
            raio = int(10 + (i / 160) * 14 + rng.integers(0, 8))
            cor = (30, 125, 190) if n % 2 == 0 else (20, 80, 120)
            cv2.circle(frame, (x, y), raio, cor, -1)

        writer.write(frame)

    writer.release()


def abrir_fonte_video(args):
    if args.demo:
        caminho_demo = Path("assets/video_teste_agrosat.mp4")
        criar_video_sintetico(caminho_demo)
        return cv2.VideoCapture(str(caminho_demo))

    if args.video:
        return cv2.VideoCapture(args.video)

    return cv2.VideoCapture(args.camera)


def main():
    parser = argparse.ArgumentParser(description="AgroSat - deteccao visual de sinais de pragas em lavouras")
    parser.add_argument("--camera", type=int, default=0, help="Indice da webcam. Padrao: 0")
    parser.add_argument("--video", type=str, help="Caminho de um video para processar")
    parser.add_argument("--demo", action="store_true", help="Executa com video sintetico de teste")
    parser.add_argument("--salvar", action="store_true", help="Salva relatorio CSV em reports/")
    args = parser.parse_args()

    captura = abrir_fonte_video(args)
    if not captura.isOpened():
        print("Erro: nao foi possivel abrir a webcam ou o video informado.")
        print("Dica: teste com: python src/detector_pragas.py --demo")
        return

    detector = AgroSatDetector()
    linhas_relatorio = []

    print("AgroSat iniciado. Pressione 'q' para sair ou 's' para salvar um print da tela.")

    while True:
        ok, frame = captura.read()
        if not ok:
            break

        frame_saida, dados = detector.inferir(frame)
        cv2.imshow("AgroSat - Monitoramento de Lavouras", frame_saida)

        if args.salvar:
            linhas_relatorio.append({
                "data_hora": datetime.now().isoformat(timespec="seconds"),
                **dados,
            })

        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord("q"):
            break
        if tecla == ord("s"):
            Path("prints").mkdir(exist_ok=True)
            nome = Path("prints") / f"agrosat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            cv2.imwrite(str(nome), frame_saida)
            print(f"Print salvo em: {nome}")

    captura.release()
    cv2.destroyAllWindows()

    if args.salvar and linhas_relatorio:
        Path("reports").mkdir(exist_ok=True)
        caminho_csv = Path("reports") / f"relatorio_agrosat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with caminho_csv.open("w", newline="", encoding="utf-8") as arquivo:
            campos = list(linhas_relatorio[0].keys())
            writer = csv.DictWriter(arquivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(linhas_relatorio)
        print(f"Relatorio salvo em: {caminho_csv}")


if __name__ == "__main__":
    main()
