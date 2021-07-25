トークテーマガチャ
====

# Django ページ構成
```
templates
├── index.html(ホーム画面)
├── base
│    └── base.html
├── common
│    ├── header.html
│    └── footer.html
├── component
│    └── navigation.html
└── product
     ├── index.html (Product一覧画面)
     └── talktheme
          └── index.html (トークテーマホーム画面)
```

## pycache 削除
```find ./ -name "__pycache__" -print | xargs rm -rf```