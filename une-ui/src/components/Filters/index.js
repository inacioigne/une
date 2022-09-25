import {
  Typography,
  Box,
  Button,
  FormGroup,
  FormControlLabel,
  Checkbox,
  Divider,
  Stack,
} from "@mui/material/";
import { useForm, Controller } from "react-hook-form";
import Facet from "./facet";
import { useSearch } from "src/providers/search";
import { useEffect, useState } from "react";

export default function Filters({ query }) {
  const { handleSubmit, control, reset } = useForm();
  const [institution, setinstitution] = useState([]);
  const [assunto, setAssunto] = useState([]);
  const [autor, setAutor] = useState([]);
  const [ano, setAno] = useState([]);
  const [tipo, setTipo] = useState([]);

  const {
    getData,
    facetInstitution,
    facetSuject,
    facetAuthor,
    facetYear,
    facetType,
    filter
  } = useSearch();

  const onSubmit = () => {
    getData(query.field, query.term, 0, filter);
  };

  return (
    <Box sx={{ m: 2 }}>
      <Typography variant="h6" gutterBottom>
        Refine sua busca
      </Typography>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Button mb={1} variant="outlined" type="submit">
          Filtrar
        </Button>
        <Stack mt={2}>
         {/* BIBLIOTECA */}
         <Facet
             metadata={"institution"}
             subject={"Biblioteca"}
             facetSuject={facetInstitution}
             control={control}
             state={institution}
             setState={setinstitution}
          /> 
            {/* ASSUNTO */}
           <Facet
             metadata={"subject"}
             subject={"Assunto"}
             facetSuject={facetSuject}
             control={control}
             state={assunto}
             setState={setAssunto}
          /> 
          {/* AUTOR */}
          <Facet
            metadata={"author"}
            subject={"Autor"}
            facetSuject={facetAuthor}
            control={control}
            state={autor}
            setState={setAutor}
          />
           {/* Ano */}
           <Facet
            metadata={"year"}
            subject={"Ano"}
            facetSuject={facetYear}
            control={control}
            state={ano}
            setState={setAno}
          />
           {/* Ano */}
           <Facet
            metadata={"type"}
            subject={"Tipo"}
            facetSuject={facetType}
            control={control}
            state={tipo}
            setState={setTipo}
          />
        </Stack>
      </form>
    </Box>
  );
}
