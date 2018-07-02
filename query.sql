SELECT dex.form
FROM dex_lexems dex
JOIN dex_definitions_lexems def_lex ON def_lex.lexemid = dex.id
JOIN dex_definitions_extra extra ON extra.id = def_lex.defid
JOIN dex_sources source ON source.id = extra.source_id 
WHERE 1 AND source.id = 27
ORDER BY dex.form;