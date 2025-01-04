FROM python:3.10-slim

ARG USERNAME=jupyter
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# システムパッケージのインストール
RUN apt-get update && apt-get install -y \
    git \
    curl \
    sudo \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# ユーザー設定
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Matplotlibの設定ディレクトリを作成し、権限を設定
RUN mkdir -p /home/$USERNAME/.config/matplotlib \
    && chown -R $USERNAME:$USERNAME /home/$USERNAME/.config \
    && chmod -R 777 /home/$USERNAME/.config

# ワークスペース設定
RUN mkdir -p /workspace \
    && chown -R $USERNAME:$USERNAME /workspace

WORKDIR /workspace

# Pythonパッケージのインストール
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER $USERNAME

# matplotlibrcをコピーして権限を設定
COPY --chown=$USERNAME:$USERNAME matplotlibrc /home/$USERNAME/.config/matplotlib/
RUN chmod 644 /home/$USERNAME/.config/matplotlib/matplotlibrc