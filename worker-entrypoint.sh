#!/bin/sh

echo "Run background workers ... "
celery -A pdf_search worker -l INFO