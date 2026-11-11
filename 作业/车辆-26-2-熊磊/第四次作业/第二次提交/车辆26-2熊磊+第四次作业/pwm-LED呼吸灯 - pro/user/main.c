/*#include "stm32f10x.h"
#include "Delay.h"
#include "PWM.h"
#include "OLED.h"

int main(void)
{
    uint16_t i;

    OLED_Init();
    PWM_Init();

while (1)
{
    for (i = 0; i < 100; i++)
    {
        PWM_SetCompare1(i);
        PWM_SetCompare2((i + 33) % 100);
        PWM_SetCompare3((i + 66) % 100);
        Delay_ms(30);
    }
}
}//流水呼吸灯
*/

#include "stm32f10x.h"
#include "Delay.h"
#include "PWM.h"
#include "OLED.h"

int main(void)
{
    uint16_t i;

    OLED_Init();
    PWM_Init();

    while (1)
    {
        // ??
        for (i = 0; i <= 100; i++)
        {
            PWM_SetCompare1(i);
            PWM_SetCompare2(i);
            PWM_SetCompare3(i);
            Delay_ms(15);   // ?????,?????
        }
        // ??
        for (i = 0; i <= 100; i++)
        {
            PWM_SetCompare1(100 - i);
            PWM_SetCompare2(100 - i);
            PWM_SetCompare3(100 - i);
            Delay_ms(15);
        }
    }
}
//三个一起呼吸灯
