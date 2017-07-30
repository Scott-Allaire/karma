import { KarmaAppPage } from './app.po';

describe('karma-app App', () => {
  let page: KarmaAppPage;

  beforeEach(() => {
    page = new KarmaAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
