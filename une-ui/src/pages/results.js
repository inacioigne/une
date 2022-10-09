import { Stack, Box, Container, Typography } from "@mui/material/";
import Grid from "@mui/material/Unstable_Grid2";
import AdvancedSearch from "src/components/advanced_search";
import { grey } from "@mui/material/colors";
import Filters from "src/components/Filters";
import CardItem from "src/components/CardItem";

import { useSearch } from "src/providers/search"

import { useRouter } from "next/router";

// React Hooks
import { useEffect, useState } from "react";

import CountUp from "react-countup";

export default function Results() {
    const router = useRouter();
  const { q } = router.query;
  const [query, setQuery] = useState({ field: "*", term: "*" });

    const { getData, numFound, items } = useSearch()

    useEffect(() => {
        
        if (!q) {
          return;
        }
    
        if (q == "all") {
          getData(query.field, query.term);
        } else {
          setQuery({ field: "marc245a", term: q });
    
          getData("marc245a", q);
        }
      }, [q]);

    return (
        <Container maxWidth="xl" >
        <AdvancedSearch getData={getData} />
        <Grid container spacing={2} sx={{ backgroundColor: grey[100] }}>
        <Grid xs={3} >
        <Filters
             //  setItems={setItems}
            //   setNumFound={setNumFound}
            //   facetSuject={facetSuject}
            //   setfacetSuject={setfacetSuject}
            //   facetAuthor={facetAuthor}
            //   setfacetAuthor={setfacetAuthor}
            //   facetYear={facetYear}
            //   setfacetYear={setfacetYear}
            //   facetType={facetType}
            //   setfacetType={setfacetType}
               query={query}
            //   page={page}
            />
            </Grid>
            <Grid
            xs={9}
            sx={{
              backgroundColor: grey[200],
              p: 3,
            }}
          >
          <Box sx={{ display: 'flex', gap: "0.5rem"}}>
          <Typography variant="h6" gutterBottom>
              <CountUp separator="." end={numFound} duration={1} /> 
            </Typography>
            <Typography variant="h6" gutterBottom>
               item encontrados
            </Typography>
            </Box>
            <Stack spacing={2}>
            {items?.map((item) => (
                <CardItem 
                    key={item.id}
                    id={item.id}
                    title={item.marc245a}
                    responsibilities={item.marc100a}
                    publisher={item.marc260b}
                    year={item.marc260c}
                    subjects={item.marc650a}
                    pages={item.marc300a}
                    chamada={item.marc090a} 
                    institution={item.institution}
                    
                />

            ))}
            </Stack>
          </Grid>
        </Grid>

        </Container>
        
    )

}