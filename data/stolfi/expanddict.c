/****************************************************************************/
/* (C) Copyright 1992 Universidade Estadual de Campinas (UNICAMP)           */
/*                    Campinas, SP, Brazil                                  */
/*                                                                          */
/* Authors:                                                                 */
/*                                                                          */
/*   Tomasz Kowaltowski  - CS Dept, UNICAMP <tomasz@dcc.unicamp.ansp.br>    */
/*   Claudio L. Lucchesi - CS Dept, UNICAMP <lucchesi@dcc.unicamp.ansp.br>  */
/*   Jorge Stolfi        - DEC Systems Research Center <stolfi@src.dec.com> */
/*                                                                          */
/* This file can be freely distributed, modified, and used for any          */
/*   non-commercial purpose, provided that this copyright and authorship    */
/*   notice be included in any copy or derived version of this file.        */
/*                                                                          */
/* DISCLAIMER: This software is offered ``as is'', without any guarantee    */
/*   as to fitness for any particular purpose.  Neither the copyright       */
/*   holder nor the authors or their employers can be held responsible for  */
/*   any damages that may result from its use.                              */
/****************************************************************************/

/* Last modified on Sun Aug  2 01:57:14 PDT 1992 by stolfi                  */

/* Expands a shrunken wordlist. 
 *
 * Usage: expanddict.c < foo.shrunk > foo
 *
 * This program assumes each line of stdin contains a word, 
 * consisting of a "prefix length", a "suffix" and a newline.
 * The prefix length is an integer in [0..35], encoded as a single
 * byte [0-9A-Z], which represents that many characters from
 * the beginning of the previous word. (In particular, the 
 * prefix lengt of the first word is zero.)  The suffix 
 * is simply the rest of the word.
 *
 * For instance, the word list
 *
 *    baby
 *    back
 *    backs
 *    backstage
 *    backup
 *    bath
 *    cobalt
 *    cobra
 *
 * would be encoded as
 *
 *    0baby
 *    2ck
 *    4s
 *    5tage
 *    4up
 *    2th
 *    0cobalt
 *    3ra
 *
 */

#include <stdio.h>

#define MAXLENGTH 1000

void main()
{
  int c, n, i;
  char w[MAXLENGTH];
  int w_len = 0;
  int bytes_read = 0;
  int bytes_written = 0;
  int words = 0;
  
  /* Loop on words: */
  while ((c = getchar()) != EOF)
    {
      ++bytes_read;
      if ((c >= '0') && (c <= '9'))
        n = c - '0';
      else if ((c >= 'A') && (c <= 'Z'))
        n = c - 'A' + 10;
      else
        { fprintf(stderr, "** bad prefix char at byte %d\n", bytes_read);
          exit(1);
        }
        
      if (n > w_len)
        { fprintf(stderr, "** bad prefix length at byte %d\n", bytes_read);
          exit(1);
        }
      
      /* Copy prefix from previous word: */
      for (i = 0; i < n; i++)
        { putchar(w[i]);
          ++bytes_written;
        };
        
      /* Copy and save rest of word: */
      while ((c = getchar()) != '\n')
        { ++bytes_read;
          putchar(c);
          ++bytes_written;
          if (n >= MAXLENGTH) 
            { fprintf(stderr, "** word too long at byte %d\n", bytes_read);
              exit(1);
            }
          w[n] = c;
          ++n;
        }
      w_len = n;
        
      /* Copy newline: */
      ++bytes_read;
      putchar('\n');
      ++bytes_written;
      ++words;
    }
  
  /* Finalize: */
  fprintf(stderr, "%8d words\n", words);
  fprintf(stderr, "%8d bytes read\n", bytes_read);
  fprintf(stderr, "%8d bytes written\n", bytes_written);

  fclose(stdout);
  fclose(stderr);
}
