# タスク管理CLIツール

Python と Poetry を使って開発された、シンプルなコマンドラインベースのタスク管理ツールです。

期限付きのタスクを追加・一覧表示できます。タスクの保存には JSON ファイルを利用しています。

---

## インストール手順

### 1. Poetry が未インストールの場合

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. リポジトリをクローン

```bash
git clone https://github.com/yourname/task_manager.git
cd task_manager
```

### 3. 依存関係をインストール

```bash
poetry install
```

## 使い方

### タスクを追加

```bash
poetry run python -m task_manager.main add --title "散歩" --due_date 2025-05-10
```

### タスクを一覧表示

```bash
poetry run python -m task_manager.main list
```

## テストの実行

このプロジェクトでは pytest を使ってユニットテストを行っています。

```bash
poetry run pytest
```
