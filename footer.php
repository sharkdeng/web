
        <footer id="site-footer" role="contentinfo" class="header-footer-group bg-dark">
            <div class="section-inner">
                <div class="footer-credits">
                    <p class="footer-copyright pr-2">&copy;
                        <?php
                        echo date_i18n(
                            /* translators: Copyright date format, see https://www.php.net/date */
                            _x( 'Y', 'copyright date format', '9scoretrain' )
                            );
                        ?>
            			
            			<a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php bloginfo( 'name' ); ?></a>
        			</p><!-- .footer-copyright -->
        			<span class="px-4"><a href="https://beian.miit.gov.cn">沪ICP备16041888-1号</a></span>
        			
        			<script type="text/javascript" src="https://s95.cnzz.com/z_stat.php?id=1260972681&web_id=1260972681"></script>
        
                </div><!-- .footer-credits -->
                
                <a class="to-the-top" href="#site-header">
                    <span class="to-the-top-long">
                        <?php
                        /* translators: %s: HTML character for up arrow. */
                        printf( __( 'To the top %s', '9scoretrain' ), '<span class="arrow" aria-hidden="true">&uarr;</span>' );
                        ?>
                    </span><!-- .to-the-top-long -->
                    <span class="to-the-top-short">
                        <?php
                        /* translators: %s: HTML character for up arrow. */
                        printf( __( 'Up %s', '9scoretrain' ), '<span class="arrow" aria-hidden="true">&uarr;</span>' );
                        ?>
                    </span><!-- .to-the-top-short -->
        		</a><!-- .to-the-top -->
        
        	</div><!-- .section-inner -->
        	
        
        </footer><!-- #site-footer -->
        
        
        <?php wp_footer(); ?>

	</body>
</html>
