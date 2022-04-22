{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "calculoporcentagem.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPcTahyPrJvMWU8/rRWf6Bk",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/driguin/AutomacoesPython/blob/main/calculoporcentagem.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-usTqA5I7oUd",
        "outputId": "96b13894-2c83-41a1-b06f-bf9b80f67670"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "QUAL A PORCENTAGEM DE REAJUSTE? 12\n",
            "12.0 % SOBRE QUAL VALOR? \n",
            " 535\n",
            " resultado:599.20\n",
            "12.0 % SOBRE QUAL VALOR? \n"
          ]
        }
      ],
      "source": [
        "n1 = float(input('QUAL A PORCENTAGEM DE REAJUSTE? '))\n",
        "\n",
        "i = 1\n",
        "\n",
        "\n",
        "\n",
        "while i < 1000 :\n",
        "\n",
        "  i = i + 1\n",
        "  print(n1 ,'% SOBRE QUAL VALOR? ')\n",
        "\n",
        "  n2 = float(input(' '))\n",
        "\n",
        "  div = n1 / 100\n",
        "\n",
        "  multi = div * n2\n",
        "  \n",
        "  resultado = multi + n2\n",
        "\n",
        "\n",
        "  print(f\" resultado:{resultado:,.2f}\")"
      ]
    }
  ]
}
